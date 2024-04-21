import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { ProductListComponent } from './product-list/product-list.component';
import { AuthorizationComponent } from './authorization/authorization.component';
import { CartComponent } from './cart/cart.component';
import { ProductDetailComponent } from './product-detail/product-detail.component';

export const routes: Routes = [
    {path: '', redirectTo: 'home', pathMatch: 'full'},
    {path: 'home', component: HomeComponent},
    {path: 'products', component: ProductListComponent},
    {path: 'auth', component: AuthorizationComponent},
    {path: 'cart', component: CartComponent},
    {path: 'products/:id', component: ProductDetailComponent}
];
