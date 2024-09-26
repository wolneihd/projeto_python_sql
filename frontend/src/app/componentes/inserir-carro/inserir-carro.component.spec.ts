import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InserirCarroComponent } from './inserir-carro.component';

describe('InserirCarroComponent', () => {
  let component: InserirCarroComponent;
  let fixture: ComponentFixture<InserirCarroComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [InserirCarroComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(InserirCarroComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
