import { Routes } from '@angular/router';
import {HomeComponent} from "./home/home.component";
import {ProductListComponent} from "./product-list/product-list.component";
import {CategoryListComponent} from "./category-list/category-list.component";
import {CartComponent} from "./cart/cart.component";

export const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent, title: 'HeadHunter' },
  { path: 'products', component: ProductListComponent, title: 'Products' },
  { path: 'categories', component: CategoryListComponent, title: 'Categories' },
  { path: 'cart', component: CartComponent, title: 'Cart' },



];
