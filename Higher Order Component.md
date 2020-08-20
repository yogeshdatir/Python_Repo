Higher Order Component

portfolio_management\src\components\watchlists\common\PrivateRoute.js

```react
import React from 'react'
import { connect } from 'react-redux'
import { Route } from 'react-router'

const PrivateRoute = ({ component: Component, auth, ...rest }) => (
	<Route
		{...rest}
		render={(props) => {
			return <Component {...props} />
		}}
	/>
)

const mapStateToProps = (state) => ({
	auth: state.auth
})

export default connect()(PrivateRoute)

```

portfolio_management\src\components\App.js

```react
import React, { Component, Fragment } from 'react'
import ReactDOM from 'react-dom'

import { Provider } from 'react-redux'
import store from '../store'
import Dashboard from './watchlists/Dashboard'

import { HashRouter as Router, Switch, Route, Redirect } from 'react-router-dom'
import Login from './watchlists/accounts/Login'
import Register from './watchlists/accounts/Register'
import Header from './watchlists/layout/Header'
import PrivateRoute from './watchlists/common/PrivateRoute'

class App extends Component {
	render() {
		return (
			<Provider store={store}>
				<Router>
					<Fragment>
						<Header />
						<PrivateRoute path="/" exact component={Dashboard} />
						<Route path="/login" exact component={Login} />
						<Route path="/register" exact component={Register} />
					</Fragment>
				</Router>
			</Provider>
		)
	}
}

ReactDOM.render(<App />, document.getElementById('app'))
```

