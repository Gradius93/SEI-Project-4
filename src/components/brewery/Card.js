import React from 'react'

const Card = ({ name, founded, area, logo }) => {
  return (
    <div className="card">
      <div className="card-header">
        <h3 className="card-header-title">{name}</h3>
      </div>
      <div className="card-image">
        <figure className="image">
          <img src={logo} alt={name} />
        </figure>
      </div>
      <div className="card-content">
        <div className="content">
          <p>{area} - {founded}</p>
        </div>
      </div>
    </div>
  )
}

export default Card
