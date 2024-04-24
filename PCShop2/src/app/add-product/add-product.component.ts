import {Component, OnInit} from '@angular/core';
import {FormsModule} from "@angular/forms";
import {ProductService} from "../services/product.service";
import {Product} from "../models/models";

@Component({
  selector: 'app-add-product',
  standalone: true,
  imports: [
    FormsModule
  ],
  templateUrl: './add-product.component.html',
  styleUrl: './add-product.component.css'
})
export class AddProductComponent implements OnInit {
  newProduct: Product = {
    id: 0,
    name: '',
    description: '',
    price: 0,
    image: '',
    quantity: 0,
    rating: 0,
    category_id: 0
  };

  constructor(private productService: ProductService) {}

  ngOnInit(): void {}

  addProduct(): void {
    this.productService.postProduct(this.newProduct)
      .subscribe(() => {
        console.log('Product added successfully');
        // Clear the form after successful addition
        this.newProduct = {
          id: 0,
          name: '',
          description: '',
          price: 0,
          image: '',
          quantity: 0,
          rating: 0,
          category_id: 0
        };
      });
  }
}
