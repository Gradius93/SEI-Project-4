import React from 'react'

const Card = ({ name, founded, area }) => {
  return (
    <div className="card">
      <div className="card-header">
        <h3 className="card-header-title">{name}</h3>
      </div>
      <div className="card-content">
        <div className="content">
          <p>{area}</p>
          <p>{founded}</p>
        </div>
      </div>
    </div>
  )
}

export default Card
