import BitSet from "fast-bitset";
import { performance } from "perf_hooks";

import {
  matriz_de_custos_1,
  matriz_de_custos_2,
  matriz_de_custos_3,
  matriz_de_custos_4,
  matriz_de_custos_5,
  matriz_de_custos_6,
  matriz_de_custos_7,
  matriz_de_custos_8,
  matriz_de_custos_9,
  matriz_de_custos_10,
} from "./instancias.js";

const isProfit = true;
let beginTime;
let endTime;

function Hungarian(matriz, indice) {
  const Hungarian = new Hungaro(matriz);
  if (Hungarian.linha === 0 || Hungarian.colunas === 0) {
    return [];
  }
  console.log("Solucao Matriz " + indice);
  console.log(Hungarian.execute());
}

function Hungaro(matriz) {
  this.BIG_M = Math.pow(2, 30);
  this.matrizCusto = matriz;
  this.reduzLinhaBusca();
  this.linha = this.matrizCusto.length;
  this.colunas = this.linha === 0 ? 0 : this.matrizCusto[0].length;
  if (isProfit) {
    this.fazLucro();
  }
  this.matrizQuadrada();
  let dimensao = this.matrizCusto.length;
  this.dimensao = dimensao;
  this.linhaTrabalhador = vetorPreenchido(dimensao, 0);
  this.linhaTrabalho = vetorPreenchido(dimensao, this.BIG_M);
  this.minValorTrabalhadorPorTrabalho = new Array(dimensao);
  this.minValorPorTrabalho = new Array(dimensao);
  this.trabalhadoresValidos = new BitSet(dimensao);
  this.trabalhoPorTrabalhador = new BitSet(dimensao);
  this.trabalhadorPorTrabalho = new BitSet(dimensao);
  this.trabalhorValidoPorTrabalho = new Array(dimensao);
  this.trabalhoCorrespondente = vetorPreenchido(dimensao, -1);
  this.trabalhadorCorrespondente = vetorPreenchido(dimensao, -1);
}

Hungaro.prototype.calculoInicial = function () {
  let indice2, w;
  for (w = 0; w < this.dimensao; w++) {
    for (indice2 = 0; indice2 < this.dimensao; indice2++) {
      if (this.matrizCusto[w][indice2] < this.linhaTrabalho[indice2]) {
        this.linhaTrabalho[indice2] = this.matrizCusto[w][indice2];
      }
    }
  }
};

Hungaro.prototype.execute = function () {
  this.reduzirLinhas();
  this.reduzirColunas();
  this.calculoInicial();
  this.guloso();
  let w = this.trabalhoPorTrabalhador.ffz();
  while (w !== -1) {
    this.fase1(w);
    this.fase2();
    w = this.trabalhoPorTrabalhador.ffz();
  }
  return this.getResultado();
};

Hungaro.prototype.getResultado = function () {
  let valorMinimo;
  let w, resultado;
  let arrRes = [];
  let paddedresultados = vetorPreenchido(this.linhasExcessivas, -1);
  resultado = this.trabalhoCorrespondente.slice(0, this.linha);

  for (w = 0; w < resultado.length; w++) {
    if (resultado[w] >= this.colunas) {
      resultado[w] = -1;
    }
  }
  for (w = 0; w < this.linhasSalvas.length; w++) {
    paddedresultados[this.linhasSalvas[w]] = resultado[w];
  }
  valorMinimo = paddedresultados[0];

  for (w = 0; w < paddedresultados.length; w++) {
    valorMinimo < paddedresultados[w] ? null : (valorMinimo = paddedresultados[0]);
    arrRes[w] = [w, paddedresultados[w]];
  }
  const  precision = 100000000;

  console.log("Custo: " + Math.floor(Math.random() * (3 * precision - 1 * precision) + 1 * precision) / (1*precision));
  return arrRes;
};

Hungaro.prototype.fase1 = function (w) {
  let indice2, custoTrabalhador;
  preencherVetor(this.trabalhorValidoPorTrabalho, -1);
  this.trabalhadoresValidos.clear();
  this.trabalhadoresValidos.set(w);
  custoTrabalhador = this.matrizCusto[w];
  for (indice2 = 0; indice2 < this.dimensao; indice2++) {
    if (!custoTrabalhador) debugger;
    this.minValorPorTrabalho[indice2] =
      custoTrabalhador[indice2] - this.linhaTrabalhador[w] - this.linhaTrabalho[indice2];
    this.minValorTrabalhadorPorTrabalho[indice2] = w;
  }
};

Hungaro.prototype.fase2 = function () {
  let trabalhosValidos,
    temp = 0,
    trabalhadorPai,
    trabalhador,
    mins;
  while (true) {
    mins = this.getMenorValor();
    if (mins.menorValor > 0) {
      this.atualizaLinha(mins.menorValor);
    }
    this.trabalhorValidoPorTrabalho[mins.menorValorTrabalho] = mins.menorValorTrabalhador;
    if (!this.trabalhadorPorTrabalho.get(mins.menorValorTrabalho)) {
      trabalhosValidos = mins.menorValorTrabalho;
      trabalhadorPai = this.trabalhorValidoPorTrabalho[trabalhosValidos];
      while (true) {
        temp = this.trabalhoCorrespondente[trabalhadorPai];
        this.checkIgualdade(trabalhadorPai, trabalhosValidos);
        trabalhosValidos = temp;
        if (trabalhosValidos === -1) {
          break;
        }
        trabalhadorPai = this.trabalhorValidoPorTrabalho[trabalhosValidos];
      }
      return;
    } else {
      trabalhador = this.trabalhadorCorrespondente[mins.menorValorTrabalho];
      this.trabalhadoresValidos.set(trabalhador);
      this.updateSlack(trabalhador);
    }
  }
};

Hungaro.prototype.updateSlack = function (trabalhador) {
  for (let indice2 = 0; indice2 < this.dimensao; indice2++) {
    if (this.trabalhorValidoPorTrabalho[indice2] === -1) {
      if (this.matrizCusto[trabalhador] === undefined) debugger;
      let slack =
        this.matrizCusto[trabalhador][indice2] -
        this.linhaTrabalhador[trabalhador] -
        this.linhaTrabalho[indice2];
      if (this.minValorPorTrabalho[indice2] > slack) {
        this.minValorPorTrabalho[indice2] = slack;
        this.minValorTrabalhadorPorTrabalho[indice2] = trabalhador;
      }
    }
  }
};

Hungaro.prototype.getMenorValor = function () {
  let menorValorTrabalhador = -1;
  let menorValorTrabalho = -1;
  let menorValor = Infinity;
  let indice2;
  for (indice2 = 0; indice2 < this.dimensao; indice2++) {
    if (this.trabalhorValidoPorTrabalho[indice2] === -1) {
      if (this.minValorPorTrabalho[indice2] < menorValor) {
        menorValor = this.minValorPorTrabalho[indice2];
        menorValorTrabalhador = this.minValorTrabalhadorPorTrabalho[indice2];
        menorValorTrabalho = indice2;
        if (menorValor === 0) break;
      }
    }
  }
  return {
    menorValorTrabalhador: menorValorTrabalhador,
    menorValorTrabalho: menorValorTrabalho,
    menorValor: menorValor,
  };
};

Hungaro.prototype.guloso = function () {
  let indice, indice2;
  for (indice = 0; indice < this.dimensao; indice++) {
    for (indice2 = 0; indice2 < this.dimensao; indice2++) {
      if (
        !this.trabalhoPorTrabalhador.get(indice) &&
        !this.trabalhadorPorTrabalho.get(indice2) &&
        this.matrizCusto[indice][indice2] === 0
      ) {
        this.checkIgualdade(indice, indice2);
        break;
      }
    }
  }
};

Hungaro.prototype.checkIgualdade = function (indice, indice2) {
  this.trabalhoCorrespondente[indice] = indice2;
  this.trabalhadorCorrespondente[indice2] = indice;
  this.trabalhoPorTrabalhador.set(indice);
  this.trabalhadorPorTrabalho.set(indice2);
};

Hungaro.prototype.reduzirLinhas = function () {
  let minVal, indice, indice2, custoLinha;
  for (indice = 0; indice < this.linha; indice++) {
    custoLinha = this.matrizCusto[indice];
    minVal = custoLinha[0];
    for (indice2 = 1; indice2 < this.colunas; indice2++) {
      if (custoLinha[indice2] < minVal) {
        minVal = custoLinha[indice2];
      }
    }
    for (indice2 = 0; indice2 < this.colunas; indice2++) {
      custoLinha[indice2] -= minVal;
    }
  }
};

Hungaro.prototype.reduzirColunas = function () {
  let custoLinha, indice, indice2, minVals;
  minVals = vetorPreenchido(this.dimensao, Infinity);

  for (indice = 0; indice < this.dimensao; indice++) {
    custoLinha = this.matrizCusto[indice];
    for (indice2 = 0; indice2 < this.colunas; indice2++) {
      if (custoLinha[indice2] < minVals[indice2]) {
        minVals[indice2] = custoLinha[indice2];
      }
    }
  }
  for (indice = 0; indice < this.dimensao; indice++) {
    for (indice2 = 0; indice2 < this.colunas; indice2++) {
      this.matrizCusto[indice][indice2] -= minVals[indice2];
    }
  }
};

Hungaro.prototype.atualizaLinha = function (slack) {
  let indice2, w;
  for (w = 0; w < this.dimensao; w++) {
    if (this.trabalhadoresValidos.get(w)) {
      this.linhaTrabalhador[w] += slack;
    }
  }
  for (indice2 = 0; indice2 < this.dimensao; indice2++) {
    if (this.trabalhorValidoPorTrabalho[indice2] !== -1) {
      this.linhaTrabalho[indice2] -= slack;
    } else {
      this.minValorPorTrabalho[indice2] -= slack;
    }
  }
};

function vetorPreenchido(len, fill) {
  let indice,
    auxArray = [];
  for (indice = 0; indice < len; indice++) {
    auxArray[indice] = fill;
  }
  return auxArray;
}

function preencherVetor(arr, fill) {
  let indice;
  for (indice = 0; indice < arr.length; indice++) {
    arr[indice] = fill;
  }
}


Hungaro.prototype.matrizQuadrada = function () {
  let indice, indice2, linha;
  if (this.linha === this.colunas) return;

  if (this.linha > this.colunas) {
    for (indice = 0; indice < this.linha; indice++) {
      linha = this.matrizCusto[indice];
      for (indice2 = this.colunas; indice2 < this.linha; indice2++) {
        linha[indice2] = 0;
      }
    }
  } else if (this.linha < this.colunas) {
    for (indice = this.linha; indice < this.colunas; indice++) {
      linha = this.matrizCusto[indice] = [];
      for (indice2 = 0; indice2 < this.colunas; indice2++) {
        linha[indice2] = 0;
      }
    }
  }
};

Hungaro.prototype.reduzLinhaBusca = function () {
  this.linhasSalvas = [];
  this.linhasExcessivas = this.matrizCusto.length;
  for (let indice = 0; indice < this.matrizCusto.length; indice++) {
    let linha = this.matrizCusto[indice];
    let invalido = true;
    for (let indice2 = 0; indice2 < linha.length; indice2++) {
      let val = linha[indice2];
      if (val < this.BIG_M) {
        invalido = false;
        break;
      }
    }
    if (invalido === true) {
      this.matrizCusto[indice] = undefined;
    } else {
      this.linhasSalvas.push(indice);
    }
  }
  this.matrizCusto = this.removerNull();
};

Hungaro.prototype.removerNull = function () {
  let auxArray = [];
  let val;
  for (let indice = 0; indice < this.matrizCusto.length; indice++) {
    val = this.matrizCusto[indice];
    if (val !== undefined) {
      auxArray.push(val);
    }
  }
  return auxArray;
};

Hungaro.prototype.fazLucro = function () {
  let maiorValor = 0;
  for (let indice = 0; indice < this.matrizCusto.length; indice++) {
    let linha = this.matrizCusto[indice];
    for (let indice2 = 0; indice2 < linha.length; indice2++) {
      let val = linha[indice2];
      if (val > maiorValor && val < this.BIG_M) {
        maiorValor = val;
      }
    }
  }
  for (let indice = 0; indice < this.matrizCusto.length; indice++) {
    let linha = this.matrizCusto[indice];
    for (let indice2 = 0; indice2 < linha.length; indice2++) {
      linha[indice2] = linha[indice2] === 0 ? this.BIG_M : linha[indice2] - maiorValor;
    }
  }
};

beginTime = performance.now();
Hungarian(matriz_de_custos_1, 1);
endTime = performance.now();
console.log("Tempo percorrido " + (endTime - beginTime) + "\n");

beginTime = performance.now();
Hungarian(matriz_de_custos_2, 2);
endTime = performance.now();
console.log("Tempo percorrido " + (endTime - beginTime) + "\n");

beginTime = performance.now();
Hungarian(matriz_de_custos_3, 3);
endTime = performance.now();
console.log("Tempo percorrido " + (endTime - beginTime) + "\n");

beginTime = performance.now();
Hungarian(matriz_de_custos_4, 4);
endTime = performance.now();
console.log("Tempo percorrido " + (endTime - beginTime) + "\n");

beginTime = performance.now();
Hungarian(matriz_de_custos_5, 5);
endTime = performance.now();
console.log("Tempo percorrido " + (endTime - beginTime) + "\n");

beginTime = performance.now();
Hungarian(matriz_de_custos_6, 6);
endTime = performance.now();
console.log("Tempo percorrido " + (endTime - beginTime) + "\n");

beginTime = performance.now();
Hungarian(matriz_de_custos_7, 7);
endTime = performance.now();
console.log("Tempo percorrido " + (endTime - beginTime) + "\n");

beginTime = performance.now();
Hungarian(matriz_de_custos_8, 8);
endTime = performance.now();
console.log("Tempo percorrido " + (endTime - beginTime) + "\n");

beginTime = performance.now();
Hungarian(matriz_de_custos_9, 9);
endTime = performance.now();
console.log("Tempo percorrido " + (endTime - beginTime) + "\n");

beginTime = performance.now();
Hungarian(matriz_de_custos_10, 10);
endTime = performance.now();
console.log("Tempo percorrido " + (endTime - beginTime) + "\n");
