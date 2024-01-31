import Select from "react-select/creatable";
import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import z from "zod";

const schema = z.object({
  contactInfo: z
    .string()
    .refine(
      (value) =>
        value.match(/^(?:(?:(?:\+|0{0,2})91[\s-]?)|[0]?)?[789]\d{9}$/) ||
        value.match(/^\S+@\S+$/),
      {
        message:
          "Invalid input. Must be a valid phone number or email address.",
      }
    ),
});

const testData = [
  "john.doe@example.com",
  "jane.smith@example.com",
  "alice.johnson@example.com",
  "bob.wilson@example.com",
  "9876543210",
];

const App = () => {
  const {
    register,
    handleSubmit,
    setValue,
    formState: { errors },
  } = useForm({
    resolver: zodResolver(schema),
  });

  const onSubmit = (data) => {
    // Handle form submission
    console.log(data);
  };

  const getSuggestions = (inputValue) => {
    const regex = new RegExp(inputValue, "i");
    return testData.filter((item) => item.match(regex));
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <label>Enter phone number or email:</label>
      <Select
        {...register("contactInfo")}
        onChange={(selectedOption) =>
          setValue("contactInfo", selectedOption?.value)
        }
        options={getSuggestions(register("contactInfo").value).map(
          (suggestion) => ({
            label: suggestion,
            value: suggestion,
          })
        )}
        isSearchable
        placeholder="Search ..."
        isClearable
        isCreatable
        formatCreateLabel={(inputValue) => `search ${inputValue}`}
      />
      {errors?.contactInfo && (
        <p style={{ color: "red" }}>{errors.contactInfo.message}</p>
      )}
      <button type="submit">Submit</button>
    </form>
  );
};

export default App;
