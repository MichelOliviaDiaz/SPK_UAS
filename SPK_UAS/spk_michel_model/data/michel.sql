--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: laptop; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.laptop (
    id integer,
    nama_produk text,
    harga_per_unit text,
    processor text,
    ram text,
    ukuran_layar text,
    storage text
);


ALTER TABLE public.laptop OWNER TO postgres;

--
-- Data for Name: laptop; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.laptop (id, nama_produk, harga_per_unit, processor, ram, ukuran_layar, storage) FROM stdin;
1	Acer Nitro 5	10.999.000	Intel Core i5 12500H	8 GB	15 inch	512GB
2	Acer Swift X (SFX14-41G)	13.649.000	Ryzen 5 5600U	16 GB	14 inch	512GB
3	Acer Aspire 5 Slim A514-54G	6.548.000	Intel Core i3 1115G4	8 GB	14 inch	512GB
4	Acer Aspire Vero	9.650.000	Intel Core i5 3.2 GHz	8 GB	15.6 inch	512GB
5	Acer Spin 5	13.349.000	Intel Core i3 1115G4	8 GB	14 inch	512GB
6	Acer Aspire Slim 3 A314-36M-36ZH	6.955.000	Intel Core i3 N305 3.80GHz	4 GB	11.6 inch	500GB
7	Acer Spin 1 SP111-33	5.589.000	Intel Celeron 1.80GHz	4 GB	11.6 inch	500GB
8	Acer Nitro 5 AN515-58-78PT	17.199.000	Intel Core i7 12700H	8 GB	15.6 inch	512GB
9	Acer Chromebook 14	4.899.000	Intel Celeron 1.80GHz	4 GB	14 inch	32GB
10	Acer Nitro 5 AN515-58-710Q	20.499.000	Intel Core i7 12650H	16 GB	15.6 inch	512GB
\.


--
-- PostgreSQL database dump complete
--

