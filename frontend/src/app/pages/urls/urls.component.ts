import { Component, OnInit } from '@angular/core';
import { LoginService } from 'src/app/services/login.service';
import { LocalstorageService } from 'src/app/services/localstorage.service';
import { Router } from '@angular/router';
import { UrlService } from 'src/app/services/url.service';

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
  urls : Array<any> = []
  domain: string = 'http://localhost:5000/u/'
  constructor(
    private loginService : LoginService,
    private localStorage : LocalstorageService,
    private urlService : UrlService,
    private router : Router 
  ) {
    this.login = this.localStorage.jwt !== '' ? false : true
    this.urlService.getAllUrls()
    .subscribe(
      data => this.loadData( data ),
      error => this.error = error.error.message
    )
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

  loadData( data ){
    console.log( data.data  )
    this.urls = data.data 
  }

  open( url ){
    window.open(this.domain + url ,'_blank')
  }

}
