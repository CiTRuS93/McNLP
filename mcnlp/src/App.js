import Loader from "react-loader-spinner";
import "./App.css";
import React, { useState, useEffect } from "react";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import axios from "axios";

function App() {
  const [temp, setTemp] = useState(0);
  const [max, setmax] = useState(0);
  const [stringToStart, setStringToStart] = useState("");
  const [rap, setRap] = useState("");
  const [wait, setWait] = useState(false);
  const [count, setCount] = useState(0);
  const tick = () => {
    setCount((prevState) => (prevState < 15 ? prevState + 1 : 0));
  };

  let timer = setInterval(() => tick(), 1000);
  clearInterval(timer);

  function submit() {
    console.log(stringToStart);
    console.log(max);
    console.log(temp);
    axios
      .post(`https://mcnlp.herokuapp.com/generate`, {
        string_to_start: stringToStart,
        max_length: max,
        temperature: temp,
      })
      .then((res) => {
        console.log(res);
        // setRap(res.data.rap)
        setWait(true);
        timer = setInterval(() => tick(), 1000);
      });
  }
  useEffect(() => {
    if (count === 0 && wait) {
      axios.get("https://mcnlp.herokuapp.com/getres").then((res) => {
        if (res.data.ready) {
          clearInterval(timer);
          setRap(res.data.rap);
          setWait(false);
        }
        if (res && res.content) {
        }
      });
    }
  }, [count, wait,timer]);

  return (
    <div className="App">
      <header className="App-header">
        <p>אורך מקסימלי (בתווים)</p>
        <TextField
          id="standard-number"
          label="max length"
          type="number"
          InputLabelProps={{
            shrink: true,
          }}
          onChange={(e) => setmax(e.currentTarget.value)}
        />
        <h7>ככל שהטמפרטורה גבוהה יותר נקבל טקסט מגוון יותר, ניתן לשחק עם הפרמטר הזה</h7>
        <TextField
          id="filled-search"
          label="temp"
          type="search"
          variant="filled"
          onChange={(e) => setTemp(e.currentTarget.value)}
        />
        
        <TextField
          id="filled-search"
          label="שורה להתחלה"
          type="search"
          variant="filled"
          onChange={(e) => setStringToStart(e.currentTarget.value)}
        />
        <Button variant="contained" onClick={() => submit()}>
          Submit
        </Button>
        <Loader type="Oval" color="#00BFFF" height={80} width={80} visible={wait}/>
        <div className="rap">
        <h6>
          {" "}
          {rap.split("\n").map((item, key) => {
            return (
              <span key={key}>
                {item}
                <br />
              </span>
            );
          })}
        </h6>
        </div>
      </header>
      <a href="https://github.com/CiTRuS93/McNLP">לעוד מידע</a>
    </div>
  );
}

export default App;
