import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment'
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  config: Object = { headers: new HttpHeaders().set('Content-Type', 'application/json') }
  constructor(
    private http: HttpClient
  ) { }

  login( email: string, password: string ): Observable<any>{
    const url = `${ environment.apiURL }/user/login`    
    return this.http.post( url, {
      email, 
      password
    }, this.config )
  }

  register( email: string, password: string ): Observable<any>{
    const url = `${ environment.apiURL }/user/register`    
    return this.http.post( url, {
      email, 
      password
    }, this.config )
  }
}
