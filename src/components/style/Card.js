import React from 'react'

const Card = ({ name }) => {
  return (
    <div className="card">
      <div className="card-header">
        <h3 className="card-header-title">{name}</h3>
      </div>
    </div>
  )
}

export default Card
