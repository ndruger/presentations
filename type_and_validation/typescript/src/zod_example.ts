import { z } from "zod";

const UserSchema = z.object({
  fieldA: z.string(),
  fieldB: z.number().int().optional(),
});

const user = UserSchema.parse({ fieldA: "a", fieldB: "1" });
// この時点で、userの型は以下のようになる
// const {
//    fieldA: string;
//    fieldB?: number | undefined;
// }
// user.fieldC = "c"; // これはエラーになる
console.log(user);
