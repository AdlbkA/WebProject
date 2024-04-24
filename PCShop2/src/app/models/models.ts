export interface AuthToken {
  access: string;
};

export interface SignUpToken {
  username: string;
  first_name: string;
  last_name: string;
  password: string;
  email: string;
};

export interface Product {
  id:number
  name: string;
  description:string;
  price: number;
  image: string;
  quantity: number;
  rating: number;
  category_id:number;
};


export interface Category{
  id:number
  name: string;
}

export interface CartItem {
  id: any;
  product: number;
  quantity: number;
}

export interface Cart {
  items: CartItem[];
  enrichedItems?: any[];
}



