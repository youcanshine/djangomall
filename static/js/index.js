import React, { useState } from 'react'
import ReactDOM from 'react-dom'

import { Example } from './components/example'

document.addEventListener('DOMContentLoaded', () => {
    ReactDOM.render(<Example />, document.getElementById('app'))
})
