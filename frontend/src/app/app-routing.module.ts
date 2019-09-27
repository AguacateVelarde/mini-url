import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { UrlsComponent } from './pages/urls/urls.component';

const routes: Routes = [
  { path : '', component: HomeComponent },
  { path : 'mis-urls', component : UrlsComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
