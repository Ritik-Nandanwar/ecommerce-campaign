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

-- Product reviews entry queries
INSERT INTO product_reviews (product_id,product_rating,product_review,date_recorded,shopper_id)
VALUES ('3000000','***','pretty awful','07/05/2018','10012');


INSERT INTO product_reviews (product_id,product_rating,product_review,date_recorded,shopper_id)
VALUES ('3007689','**','disappointing','07/05/2018','10009');

INSERT INTO product_reviews (product_id,product_rating,product_review,date_recorded,shopper_id)
VALUES ('3007779','****','decent','07/05/2018','10008');

INSERT INTO product_reviews (product_id,product_rating,product_review,date_recorded,shopper_id)
VALUES ('3007937','*****','if in need of this product , go ahead with it','07/05/2018','10020');

INSERT INTO product_reviews (product_id,product_rating,product_review,date_recorded,shopper_id)
VALUES ('3006033','*','broke down in 3 days','07/05/2018','10010');

INSERT INTO product_reviews (product_id,product_rating,product_review,date_recorded,shopper_id)
VALUES ('3000021','****','could be better','07/05/2018','10021');

INSERT INTO seller_reviews (seller_id,seller_rating,seller_review,date_recorded,shopper_id)
VALUES('200004','***','delivery arrived quickly but damaged','01/06/2018','10008');

INSERT INTO seller_reviews (seller_id,seller_rating,seller_review,date_recorded,shopper_id)
VALUES('200011','**','late delivery, missing items','07/03/2018','10012');

INSERT INTO seller_reviews (seller_id,seller_rating,seller_review,date_recorded,shopper_id)
VALUES('200010','****','fast delivery, excellent service','04/02/2014','10020');

INSERT INTO seller_reviews (seller_id,seller_rating,seller_review,date_recorded,shopper_id)
VALUES('200007','**','never responded to late package queries, refund issued.','06/09/2017','10021');

INSERT INTO seller_reviews (seller_id,seller_rating,seller_review,date_recorded,shopper_id)
VALUES('200002','*****','excellent customer service, timely delivery, great product','03/02/2019','10009');

INSERT INTO product_Q (product_id,question,date_recorded)
VALUES('3007717','how does it smell?','01/02/2015');

INSERT INTO product_Q (product_id,question,date_recorded)
VALUES('3007717','how does it taste?','02/01/2018');

INSERT INTO product_Q (product_id,question,date_recorded)
VALUES('3007717','does it fit in a glove box?','03/08/2014');

INSERT INTO product_Q (product_id,question,date_recorded)
VALUES('3007717','does it cause cancer?','11-11-2019');

INSERT INTO product_Q (product_id,question,date_recorded)
VALUES('3007717','is the packaging edible?','09-12-2020');

INSERT INTO product_Q (product_id,question,date_recorded)
VALUES('3007717','why does it cost so much?','04-04-2017');

INSERT INTO product_A (question_number,answer,date_recorded)
VALUES ('1','it smells like the house across the street has a stockpile of rotten eggs; distantly vile','07/03/2015');

INSERT INTO product_A (question_number,answer,date_recorded)
VALUES ('2','bland, and uninteresting','07/03/2018');

INSERT INTO product_A (question_number,answer,date_recorded)
VALUES ('2','faintly of vanilla','06/04/2019');

INSERT INTO product_A (question_number,answer,date_recorded)
VALUES ('3','most decidedly not','03/03/2015');

INSERT INTO product_A (question_number,answer,date_recorded)
VALUES ('3','perhaps; although not in one piece, and it depends on your car model','07/09/2014');

INSERT INTO product_A (question_number,answer,date_recorded)
VALUES ('4','only if you swallow it','07/03/2020');

INSERT INTO product_A (question_number,answer,date_recorded)
VALUES ('4','I sell things on an online market, how am i supposed to know?','12/12/2019');

INSERT INTO product_A (question_number,answer,date_recorded)
VALUES ('5','yes, but only once','12/12/2020');

INSERT INTO product_A (question_number,answer,date_recorded)
VALUES ('5','a tad chewy for my tastes, although I cannot speak for your preferences','10/12/2020');

INSERT INTO product_A (question_number,answer,date_recorded)
VALUES ('1','it does not smell much of anything, although, i do suffer from anosmia','04/04/2016');

INSERT INTO product_A (question_number,answer,date_recorded)
VALUES ('6','manufacturing costs','08/05/2018');

INSERT INTO product_A (question_number,answer,date_recorded)
VALUES ('6','an unbelievably transparent money laundering scheme','07/05/2018');

