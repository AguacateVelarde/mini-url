import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LocalstorageService {
  storage : any = window.localStorage;
  jwt : string = ''
  constructor() { 
    this.jwt =  this.storage.getItem('jwt-user') || ''
  }

  saveJWT ( jwt :string ){
    this.storage.setItem( 'jwt-user', jwt )
  }
  deleteJWT( ){
    this.storage.removeItem( 'jwt-user' )
  }
}
