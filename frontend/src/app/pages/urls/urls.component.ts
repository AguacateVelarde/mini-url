import { Component, OnInit } from '@angular/core';
import { LoginService } from 'src/app/services/login.service';
import { LocalstorageService } from 'src/app/services/localstorage.service';
import { Router } from '@angular/router';
import { UrlService } from 'src/app/services/url.service';
declare var $;
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
  url_modal:string = ''
  error_modal:string = ''
  error_login:string = ''
  error_register:string = ''
  email_register :string = ''
  password_register : string = ''
  confirm_register : string = ''

  constructor(
    private loginService : LoginService,
    private localStorage : LocalstorageService,
    private urlService : UrlService,
    private router : Router 
  ) {
    this.login = this.localStorage.jwt !== '' ? false : true
    if( !this.login ){
      this.initData()
    }
   }

  ngOnInit() {
  }

  initData( ){
    this.urlService.getAllUrls()
    .subscribe(
      data => this.loadData( data ),
      error => this.error = error.error.message
    )
  }

  doLogin(){
    if( this.email_login === '' || this.password_login === '' ){
      this.error_login = "Error con tus datos"
    }else{
      this.loginService.login( this.email_login, this.password_login )
      .subscribe( 
        data => this.loadUser( data ),
        error => this.error_login = error.error.message) 
    }
    
  }

  doRegister(){
    if( this.email_register === '' 
      || this.password_register === '' 
      || this.confirm_register === '' 
      || this.password_register !== this.confirm_register
    ){
      this.error_register = "Error con tus datos"
    }else{
      this.loginService.register( this.email_register, this.password_register )
      .subscribe( 
        data => this.loadUser( data ),
        error => this.error_register = error.error.message) 
    }
  }

  loadUser( data ){
    this.localStorage.saveJWT( data.token )
    this.login = false
    location.reload()
  }

  loadData( data ){
    this.urls = data.data 
  }

  open( url ){
    window.open(this.domain + url ,'_blank')
  }

  deleteSession(){
    this.localStorage.deleteJWT()
    location.reload()
  }
  sendUrl(){
    this.urlService.sendUrl( this.url_modal )
    .subscribe( 
      data => this.finishModal(),
      error => this.error_modal = error.error.message
    )
  }

  finishModal(){
    this.initData()
    $('#exampleModalScrollable').modal('hide')
  }
}
