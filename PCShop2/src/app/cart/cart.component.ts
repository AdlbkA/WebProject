import { Component } from '@angular/core';
import {CartService} from "../services/cart.service";

@Component({
  selector: 'app-cart',
  standalone: true,
  imports: [],
  templateUrl: './cart.component.html',
  styleUrl: './cart.component.css'
})
export class CartComponent {
  items = this.cartService.getCart();

  constructor (
    private cartService: CartService
  ) {}

  clearCart(){
    //this.items = this.cartService.removeItemFromCart();
  }
}
