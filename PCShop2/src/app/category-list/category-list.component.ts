import {Component, OnInit} from '@angular/core';
import {Category, Product} from "../models/models";
import {CategoryService} from "../services/category.service";
import {RouterLink} from "@angular/router";
import {NgFor} from "@angular/common";

@Component({
  selector: 'app-category-list',
  standalone: true,
  imports: [
    RouterLink, NgFor
  ],
  templateUrl: './category-list.component.html',
  styleUrl: './category-list.component.css'
})
export class CategoryListComponent implements OnInit{
  categories !: Category[];
  constructor(
    private categoryService: CategoryService) {

  }
  ngOnInit() {
    this.categoryService.getCategory().subscribe((categories) =>
      this.categories = categories)
  }
}
