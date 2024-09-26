import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../shared/api-service.service';
import { HttpErrorResponse } from '@angular/common/http';

interface Carro {
  id: number,
  fabricante: string,
  cor: string,
  placa: string,
  data_cadastro: string
}

@Component({
  selector: 'app-lista-carros',
  templateUrl: './lista-carros.component.html',
  styleUrl: './lista-carros.component.css'
})
export class ListaCarrosComponent implements OnInit {
  data: Carro[] = [];
  cores: any;

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.apiService.getData().subscribe(
      response => {
        this.data = response;  // Presumindo que a resposta já é um array de Carro
      },
      error => {
        console.log('Erro ao buscar dados', error);
      }
    );
  }
}
