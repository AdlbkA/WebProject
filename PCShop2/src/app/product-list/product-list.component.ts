import {Component, OnInit} from '@angular/core';
import {Product} from "../models/models";
import {ProductService} from "../services/product.service";
import {RouterLink} from "@angular/router";
import {NgFor} from "@angular/common";

@Component({
  selector: 'app-product-list',
  standalone: true,
  imports: [
    RouterLink, NgFor
  ],
  templateUrl: './product-list.component.html',
  styleUrl: './product-list.component.css'
})
export class ProductListComponent implements OnInit{
  products !: Product[];
  constructor(
    private productService: ProductService) {

  }
  ngOnInit() {
    this.productService.getProducts().subscribe((products) =>
      this.products = products)
  }
}
