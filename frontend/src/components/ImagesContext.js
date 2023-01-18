import  {createContext} from "react";

const ImagesContext = createContext({
  images: null,
  setImages: () => {}
});

export default ImagesContext;
