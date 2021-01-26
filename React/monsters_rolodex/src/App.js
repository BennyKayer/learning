import React, { Component } from "react";
import { connect } from "react-redux";
import { setSearchField } from "./actions";
import "./App.css";
import { CardList } from "./components/card-list/card-list.component";
import { SearchBox } from "./components/search-box/search-box.component";
import { requestRobots } from "./actions";

class App extends Component {
    // constructor() {
    //     super();
    //     this.state = {
    //         monsters: [],
    //         searchField: "",
    //     };
    //     //weird js things with normal funcitons
    //     //this.handleChange = this.handleChange.bind(this);
    // }

    // componentDidMount() {
    //   fetch("https://jsonplaceholder.typicode.com/users")
    //   .then(response => response.json())
    //   .then(users => this.setState({monsters : users}));
    // }

    // werid js things
    handleChange = (e) => {
        this.setState({ searchField: e.target.value });
    };

    /*async*/ componentDidMount() {
        // const response = await fetch(
        //     "https://jsonplaceholder.typicode.com/users"
        // );
        // const users = await response.json();
        // this.setState({ monsters: users });
        this.props.onRequestRobots();
    }

    render() {
        const { monsters, searchField, isPending } = this.props;
        const filteredMonsters = monsters.filter((monster) =>
            monster.name.toLowerCase().includes(searchField.toLowerCase())
        );
        return isPending ? (
            <h1>{"Pending"}</h1>
        ) : (
            <div className="App">
                <h1>Monsters Rolodex</h1>
                <SearchBox
                    placeholder="search monsters"
                    handleChange={this.handleChange}
                />
                <CardList monsters={filteredMonsters} />
            </div>
        );
    }
}

const mapStateToProps = (state) => ({
    searchField: state.searchRobots.searchField,
    robots: state.requestRobots.robots,
    isPending: state.requestRobots.isPending,
    error: state.requestRobots.error,
});

const mapDispatchToProps = (dispatch) => ({
    setSearchField: (value) => dispatch(setSearchField(value)),
    onRequestRobots: () => requestRobots(dispatch),
});

export default connect(mapStateToProps, mapDispatchToProps)(App);
