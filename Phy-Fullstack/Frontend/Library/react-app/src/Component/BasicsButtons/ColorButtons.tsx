import * as React from 'react';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';

export default function ColorButtons() {
  return (
    <Stack direction="row" spacing={2}>
      <Button color="secondary">Home</Button>
      <Button variant="contained" color="success">
        Page1
      </Button>
      <Button variant="outlined" color="error">
        Page2
      </Button>
      <Button variant="contained" color="success">
        Page3
      </Button>
    </Stack>
  );
}