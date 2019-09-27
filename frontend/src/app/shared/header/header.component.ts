import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {

  constructor(
    private route : Router
  ) { }

  ngOnInit() {
  }

  profile(){
    this.route.navigate( ['/profile'])
  }
  url(){
    this.route.navigate( ['/mis-urls'])
  }
  routeVerified(){
    return this.route.url
  }

  home(){
    this.route.navigate( ['/'])
  }
}
