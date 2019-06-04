import React from 'react'

const Card = ({ name }) => {
  return (
    <div className="card">
      <div className="card-header beerstyle">
        <h3 className="card-header-title beerstyle">{name}</h3>
      </div>
    </div>
  )
}

export default Card
