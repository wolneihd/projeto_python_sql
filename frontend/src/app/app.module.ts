import { NgModule } from '@angular/core';
import { BrowserModule, provideClientHydration } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ListaCarrosComponent } from './componentes/lista-carros/lista-carros.component';

import { provideHttpClient, withFetch } from '@angular/common/http';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { MatIconModule } from '@angular/material/icon'; // Importando MatIconModule

@NgModule({
  declarations: [
    AppComponent,
    ListaCarrosComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MatIconModule
  ],
  providers: [
    provideClientHydration(),
    provideHttpClient(withFetch()),
    provideAnimationsAsync()  // Adicione esta linha para habilitar fetch
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
