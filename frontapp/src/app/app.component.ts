import { Component } from '@angular/core';
import {ApiService} from "./api.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ApiService]
})
export class AppComponent {
  title = 'app';
  balancesheet = [{date: 213}, {date: 555}];
  constructor(private api: ApiService) {
    this.getAllBalanceSheet()
  }
  getAllBalanceSheet = () => {
    this.api.getAllBalanceSheet().subscribe(data => {
      this.balancesheet = data;
    },error => {
      console.log(error);
    })
  }
}
