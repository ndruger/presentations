const validate = require("validate.js");

const constraints = {
  fieldA: {
    presence: true,
    type: "string",
  },
  fieldB: {
    type: "integer",
  },
};

const request = { fieldA: "a", fieldB: 10 };
const invalid = validate(request, constraints);
if (invalid) {
  console.log("invalid", invalid);
}
