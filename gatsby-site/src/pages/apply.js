import React from 'react'
import Redirect from 'react-router'

import Link from 'gatsby-link'

class ApplyPage extends React.Component {

  constructor(props) {
    super(props)        
  }

  // immediately redirect to bit.ly typeform
  // 
  componentDidMount() {
    top.location="http://bit.ly/hackademy_apply"
  }

  render() {
    return (      
      <div></div>
    )
  }
}

export default ApplyPage
