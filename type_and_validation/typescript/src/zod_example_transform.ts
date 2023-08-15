import { z } from "zod";

const UserSchema = z.object({
  fieldA: z.string(),
  fieldB: z.coerce.number().int().optional(), // coerceを使うと、型が変換される
});

const user = UserSchema.parse({ fieldA: "a", fieldB: "1" }); // fieldBはstring型だが、coerceによりnumber型に変換される
console.log(user);
