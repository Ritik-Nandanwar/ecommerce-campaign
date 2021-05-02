CREATE TABLE seller_reviews (
    seller_id     INTEGER REFERENCES sellers (seller_id) 
                          PRIMARY KEY,
    seller_rating TEXT    NOT NULL,
    seller_review TEXT    NOT NULL,
    date_recorded DATE    NOT NULL,
    shopper_id    INTEGER REFERENCES shoppers (shopper_id) 
);

CREATE TABLE product_reviews (
    product_id     INTEGER REFERENCES products (product_id) 
                           PRIMARY KEY
                           NOT NULL,
    product_rating TEXT    NOT NULL,
    product_review TEXT    NOT NULL,
    date_recorded  DATE    NOT NULL,
    shopper_id     INTEGER REFERENCES shoppers (shopper_id) 
                           NOT NULL
                           UNIQUE
);

CREATE TABLE product_QnA (
    product_id INTEGER REFERENCES products (product_id) 
                            NOT NULL,
    question_number INTEGER PRIMARY KEY AUTOINCREMENT
                            UNIQUE
                            NOT NULL,
    question        TEXT    NOT NULL,
    answer          TEXT    NOT NULL
);


