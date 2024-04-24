import { Routes } from '@angular/router';
import {HomeComponent} from "./home/home.component";
import {ProductListComponent} from "./product-list/product-list.component";
import {CategoryListComponent} from "./category-list/category-list.component";
import {CartComponent} from "./cart/cart.component";
import {AuthComponent} from "./auth/auth.component";

export const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent, title: 'PCShop' },
  { path: 'products', component: ProductListComponent, title: 'Products' },
  { path: 'categories', component: CategoryListComponent, title: 'Categories' },
  { path: 'cart', component: CartComponent, title: 'Cart' },
  { path: 'login', component: AuthComponent, title: 'Auth' },
];
