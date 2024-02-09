// import useSetDBData from "./Indexdb/useSetDBData";
import { useEffect, useState } from "react";
import useGetDBData from "./indexdb/useGetDBData";
import useSetDBData from "./indexdb/useSetDBData";
const App = () => {
  const { setData } = useSetDBData();
  const [profile, setProfile] = useState(null);
  // setData({ email: "ritesh", phone_number: "1234567890", password: 12344 });
  const { getData } = useGetDBData();
  useEffect(() => {
    const getDataFromDB = async () => {
      const value = await getData("exampl@egmail.com"); //this input wil come from search field
      if (!value) {
        console.log("data is not present"); // instead showing this log do an api request
        /*
        example:
        const req = await fetch(url);
        const data = await req.json();
        setData(data)
        */
        setData({ email: "example@gmail.com", phone_number: "1234567890" }); //replace following input with data coming from api
        // setProfile({ email: "example@gmail.com", phone_number: "1234567890" });
        return;
      }
      setProfile(value);
    };
    getDataFromDB();
  }, [getData, setData]);
  console.log(profile);
  return (
    <div>
      {/* replace below code with the component which you will use for rendering  */}
      <h1>{profile?.email}</h1>
      <p>{profile?.phone_number}</p>
    </div>
  );
};

export default App;
