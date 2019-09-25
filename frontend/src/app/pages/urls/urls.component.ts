import { Component, OnInit } from '@angular/core';
import { LoginService } from 'src/app/services/login.service';
import { LocalstorageService } from 'src/app/services/localstorage.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-urls',
  templateUrl: './urls.component.html',
  styleUrls: ['./urls.component.scss']
})
export class UrlsComponent implements OnInit {
  login:boolean = true
  type : string = 'LOGIN'
  email_login :string = ''
  password_login:string = ''
  error:string = ''
  constructor(
    private loginService : LoginService,
    private localStorage : LocalstorageService,
    private router : Router 
  ) {
    this.login = this.localStorage.jwt !== '' ? false : true
   }

  ngOnInit() {
  }

  doLogin(){
    if( this.email_login === '' || this.password_login === '' ){
      this.error = "Error con tus datos"
    }else{
      this.loginService.login( this.email_login, this.password_login )
      .subscribe( 
        data => this.loadUser( data ),
        error => this.error = error.error.message) 
    }
    
  }

  loadUser( data ){
    this.localStorage.saveJWT( data.token )
    this.login = false
  }

}
