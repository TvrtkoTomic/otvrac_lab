PGDMP                     
    {            ducani_tehnike    15.2    15.2     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                        0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16744    ducani_tehnike    DATABASE     �   CREATE DATABASE ducani_tehnike WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Croatian_Croatia.1250';
    DROP DATABASE ducani_tehnike;
                postgres    false            �            1259    16745    ducani_tehnike    TABLE     g  CREATE TABLE public.ducani_tehnike (
    ducan_id bigint NOT NULL,
    naziv character varying,
    adresa character varying,
    grad character varying,
    drzava character varying,
    telefonski_broj character varying,
    email character varying,
    geolokacija character varying,
    recenzija double precision,
    postanski_broj character varying
);
 "   DROP TABLE public.ducani_tehnike;
       public         heap    postgres    false            �            1259    16750    vlasnici    TABLE     �   CREATE TABLE public.vlasnici (
    id bigint NOT NULL,
    ime character varying,
    prezime character varying,
    ducan_id bigint
);
    DROP TABLE public.vlasnici;
       public         heap    postgres    false            �          0    16745    ducani_tehnike 
   TABLE DATA           �   COPY public.ducani_tehnike (ducan_id, naziv, adresa, grad, drzava, telefonski_broj, email, geolokacija, recenzija, postanski_broj) FROM stdin;
    public          postgres    false    214   �       �          0    16750    vlasnici 
   TABLE DATA           >   COPY public.vlasnici (id, ime, prezime, ducan_id) FROM stdin;
    public          postgres    false    215   6       i           2606    16760 "   ducani_tehnike ducani_tehnike_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.ducani_tehnike
    ADD CONSTRAINT ducani_tehnike_pkey PRIMARY KEY (ducan_id);
 L   ALTER TABLE ONLY public.ducani_tehnike DROP CONSTRAINT ducani_tehnike_pkey;
       public            postgres    false    214            l           2606    16762    vlasnici vlasnici_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.vlasnici
    ADD CONSTRAINT vlasnici_pkey PRIMARY KEY (id);
 @   ALTER TABLE ONLY public.vlasnici DROP CONSTRAINT vlasnici_pkey;
       public            postgres    false    215            j           1259    16768    fki_m    INDEX     >   CREATE INDEX fki_m ON public.vlasnici USING btree (ducan_id);
    DROP INDEX public.fki_m;
       public            postgres    false    215            �   8  x�m�Kr�@���)� ż씔]��Q��Eʛ�����������!r���{��VAϙ��8\�f��K'ج��<�Z#�T���oXz��s��Э.�<͕Vl�8���3���4NRP��$*a���ʶ���z�)\u�샫�L\�h-ɣ�u��'�:�����{��Kl�k�PȦt����:�8�Hy&Dʡ�����;�7$�A���ސ�A������զ!*|�P\�_4"�¼�l8�L��i��s)�@�;ʠ���R'Cp�wF.�.�����u��O[��Y.�s	�T��1���m1��^��2��R8?��|7Ok�\ٕ!��Gsɧj��of˲k]؅7TB\A�� �X�44��v�p�Kv�4�bQO��H���*�غu>`Ә�Ċ�[Jq�MF޾mzl[���epZ���ܥ8��}�m�YEk�.�0�k�mӷN$��P�3��Z#�@�õY6�}�������IJ��YtK��B?vRc�g��ᇅ����7�2?�)�o+L�;����O+Sc��ʅ�B%i�A�s��ė������,���(��0�      �   �   x�M�MN�0��oN�Tu��%V�Q	$�f��ʉ���R +܀�%����{zwb����7�n���n�h�`�n��s*��63y������ZT���d�7�M�y')vm㰠5v<����OV,i�_{�L�+�6I���6��Eafd<�����K��rC���K|������Y�V�R��7�K�G�ɔ�|q۸��pI�S"�k�TG     