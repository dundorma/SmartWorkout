-- Adminer 4.8.1 PostgreSQL 16.2 (Debian 16.2-1.pgdg120+2) dump

\connect "smartworkout";

CREATE TABLE "public"."users" (
  "id" uuid NOT NULL,
  "email" text NOT NULL,
  "password" text NOT NULL,
  CONSTRAINT "users_email_key" UNIQUE ("email"),
  CONSTRAINT "users_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

-- 2024-03-14 16:21:22.737813+00
