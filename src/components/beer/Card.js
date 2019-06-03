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
        <div className="content level">
          <div className="level-right">
            <p>{abv}%</p>
          </div>
          <div className="level-right">
            <p className="level-left">£{price}</p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Card
