import { Component } from '@angular/core';
import {RouterLink, RouterModule, RouterOutlet} from '@angular/router';
import {ProductListComponent} from "./product-list/product-list.component";
import {HomeComponent} from "./home/home.component";
import {CategoryListComponent} from "./category-list/category-list.component";
import {CartComponent} from "./cart/cart.component";
import {AuthComponent} from "./auth/auth.component";
import {ProductDetailsComponent} from "./product-details/product-details.component";
import {FormsModule} from "@angular/forms";
import {NgIf} from "@angular/common";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink, RouterModule, ProductListComponent, HomeComponent, AuthComponent, CategoryListComponent, CartComponent, ProductDetailsComponent, FormsModule, NgIf],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'PCShop';

}

