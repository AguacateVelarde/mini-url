import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-urls',
  templateUrl: './urls.component.html',
  styleUrls: ['./urls.component.scss']
})
export class UrlsComponent implements OnInit {
  login:boolean = false
  constructor() { }

  ngOnInit() {
  }

}
