import {HttpClient, HttpErrorResponse, HttpParams} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {Observable, throwError} from 'rxjs';
import {catchError} from 'rxjs/operators';
import {Product} from '../models/models';

@Injectable({
    providedIn: 'root'
})
export class ProductService {
    private BASE_URL = 'http://localhost:8000/api/';

    constructor(private http: HttpClient) {
    }

    getProducts(): Observable<Product[]> {
        return this.http.get<Product[]>(`${this.BASE_URL}products/`);

    }

    // Handle errors
    handleError(error: HttpErrorResponse): Observable<never> {
        let errorMessage = 'Unknown error!';
        if (error.error instanceof ErrorEvent) {
            errorMessage = `Client-side Error: ${error.error.message}`;
        } else {
            errorMessage = `Server-side Error Code: ${error.status}\nMessage: ${error.message}`;
        }
        console.error('Error occurred:', errorMessage);
        return throwError(() => new Error(errorMessage));
    }


    getProductById(id: number): Observable<Product> {
        return this.http.get<Product>(`${this.BASE_URL}products/${id}`)
            .pipe(catchError(this.handleError));
    }


}
