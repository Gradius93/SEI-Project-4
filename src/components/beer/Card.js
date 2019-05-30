import React from 'react'

const Card = ({ image, name, abv, price }) => {
  return (
    <div className="card">
      <div className="card-image">
        <figure className="image">
          <img src={image} alt={name} />
        </figure>
      </div>
      <div className="card-header">
        <h3 className="card-header-title">{name}</h3>
      </div>
      <div className="card-content">
        <div className="content">
          <p>{abv} %</p>
          <p>£{price}</p>
        </div>
      </div>
    </div>
  )
}

export default Card
