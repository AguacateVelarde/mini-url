import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../environments/environment'
import { LocalstorageService } from './localstorage.service';

@Injectable({
  providedIn: 'root'
})
export class UrlService {
  config: Object
  constructor(
    private http: HttpClient,
    private localStorage : LocalstorageService
  ) { 
    this.config = { headers: new HttpHeaders()
      .set('Content-Type', 'application/json') 
      .set("Authorization", `Bearer ${ localStorage.jwt }` )
    }
  }

  sendUrl( url_user :string ){
    const url = `${ environment.apiURL }/url`    
    return this.http.post( url, {
      url : url_user
    }, this.config )
  }

  getAllUrls(){
    const url = `${ environment.apiURL }/url/all`    
    return this.http.get( url, this.config )
  }
}
