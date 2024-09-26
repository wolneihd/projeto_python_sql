import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private todosCarros = 'http://localhost:5000/'; // Substitua pela URL da API desejada
  private todasCores =  'http://localhost:5000/cores'

  constructor(private http: HttpClient) {}

  getData(): Observable<any> {
    return this.http.get<any>(this.todosCarros);
  }
}
