import React from 'react'

const Card = ({ image, name }) => {
  return (
    <div className="card">
      <div className="card-image">
        <figure className="image brew2 hover1">
          <img src={image} alt={name} />
          <div className="card-content brew-text2">
            <h3 className="card-header-title">{name}</h3>

          </div>
        </figure>
      </div>
    </div>
  )
}

export default Card
