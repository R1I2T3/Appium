import connect from "./connect";

const useSetDBData = () => {
  const setData = async (data) => {
    const db = await connect();
    if (db) {
      const transaction = db.transaction("Profiling", "readwrite");
      const action = transaction.objectStore("Profiling");
      action.add(data);
    }
  };
  return { setData };
};

export default useSetDBData;
