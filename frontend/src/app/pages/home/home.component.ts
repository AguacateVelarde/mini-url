import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { LocalstorageService } from 'src/app/services/localstorage.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  constructor(
    private route : Router,
    public localstorage : LocalstorageService
  ) { }

  ngOnInit() {
  }

  log(){
    this.route.navigate( ['/mis-urls'])
  }

}
