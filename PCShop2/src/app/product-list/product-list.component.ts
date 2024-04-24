import { Component } from '@angular/core';
import {Product} from "../models/models";
import {ProductService} from "../services/product.service";
import {RouterLink} from "@angular/router";

@Component({
  selector: 'app-product-list',
  standalone: true,
  imports: [
    RouterLink
  ],
  templateUrl: './product-list.component.html',
  styleUrl: './product-list.component.css'
})
export class ProductListComponent {
  products !: Product[];
  constructor(
    private productService: ProductService) {

  }
  ngOnInit() {
    this.productService.getProducts().subscribe((products) =>
      this.products = products)
  }
}
